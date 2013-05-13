"""
Shamelessly stolen from Django Fiber

https://github.com/ridethepony/django-fiber
"""
import operator

from django import template

from schedule.models import ExtendedFlatPage

register = template.Library()

def show_menu(context, menu_name, min_level, max_level, expand=None):
  menu_pages = []
  needed_pages = []

  try:
    root_page = ExtendedFlatPage.objects.get(title=menu_name, parent=None)
  except ExtendedFlatPage.DoesNotExist:
    raise ExtendedFlatPage.DoesNotExist("Menu does not exist.\nNo top-level page found with the title %s." % menu_name)

  # Page.get_absolute_url() accesses self.parent recursively to build URLs
  # (assuming relative URLs).
  # This means that to render any menu item, we need all the ancestors up to
  # the root. Therefore it is more efficient to pull back this tree, without
  # min_level applied, and apply it just to decide which items to render.

  current_page = None

  if "extendedflatpage" in context:
    current_page = context["extendedflatpage"]

  if current_page and current_page.is_child_of(root_page):
    tree = root_page.get_descendants(include_self=True).filter(mptt_level__lte=max_level)
    if expand == "all":
      needed_pages = tree
    else:
      if current_page.level + 1 < min_level:
        # Nothing to do
        needed_pages = []
      else:
        # We need the "route" nodes, the "sibling" nodes and the children
        route = tree.filter(mptt_left__lt=current_page.mptt_left,
                  mptt_right__gt=current_page.mptt_right)

        # We show any siblings of anything in the route to the current page.
        # The logic here is that if the user drills down, menu items
        # shown previously should not disappear.

        # The following assumes that accessing .parent is cheap, which
        # it can be if current_page was loaded correctly.
        p = current_page
        sibling_qs = []
        while p.parent_id is not None:
          sibling_qs.append(tree.filter(mptt_level=p.mptt_level,
                          mptt_left__gt=p.parent.mptt_left,
                          mptt_right__lt=p.parent.mptt_right))
          p = p.parent
        route_siblings = reduce(operator.or_, sibling_qs)

        children = tree.filter(mptt_left__gt=current_page.mptt_left,
                     mptt_right__lt=current_page.mptt_right)
        if expand != "all_descendants":
          # only want immediate children:
          children = children.filter(mptt_level=current_page.mptt_level + 1)

        needed_pages = route | route_siblings | children

  else:
    # Only show menus that start at the first level (min_level == 1)
    # when the current page is not in the menu tree.
    if min_level == 1:
      if not expand:
        needed_pages = ExtendedFlatPage.objects.filter(tree_id=root_page.tree_id).filter(mptt_level__lte=1)
      elif expand == "all":
        needed_pages = ExtendedFlatPage.objects.filter(tree_id=root_page.tree_id).filter(mptt_level__lte=max_level)
      else:
        needed_pages = []

  needed_pages = ExtendedFlatPage.objects.link_parent_objects(needed_pages)

  # Now we need to do min_level filtering
  for p in needed_pages:
    if p.mptt_level >= min_level:
      menu_pages.append(p)

  # Remove pages that shouldn"t be shown in the menu for the current user.
  #menu_pages = [p for p in menu_pages if p.show_in_menu]

  """
  Order menu_pages for use with tree_info template tag.
  """
  menu_pages = sorted(menu_pages, key=lambda menu_page: menu_page.mptt_left)

  """
  Find parent page for this menu
  """
  menu_parent_page = None
  if menu_pages:
    menu_parent_page = menu_pages[0].parent
  elif min_level == 1:
    menu_parent_page = root_page

  context["Page"] = ExtendedFlatPage
  context["menu_pages"] = menu_pages
  context["menu_parent_page"] = menu_parent_page
  context["menu_args"] = {"menu_name": menu_name, "min_level": min_level, "max_level": max_level, "expand": expand}
  return context

register.inclusion_tag("menu.html", takes_context=True)(show_menu)
