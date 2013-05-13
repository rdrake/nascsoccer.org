from mptt.managers import TreeManager

class PageManager(TreeManager):
    """Adapter from Django-Fiber"""
    def link_parent_objects(self, pages):
        """
        Given an iterable of page objects which includes all ancestors
        of any contained pages, unifies the 'parent' objects
        using items in the iterable.
        """
        pages = list(pages)
        page_dict = {}

        for p in pages:
            page_dict[p.id] = p

        for p in pages:
            if p.parent_id is None:
                p.parent = None
            else:
                p.parent = page_dict[p.parent_id]
            
            p._ancestors_retrieved = True
        
        return pages
