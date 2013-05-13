from django.contrib.flatpages.models import FlatPage

from mptt.models import MPTTModel, TreeForeignKey

from apps.cms.manager import PageManager

class ExtendedFlatPage(MPTTModel, FlatPage):
    parent = TreeForeignKey(
        "self",
        null=True,
        blank=True,
        related_name="children"
    )
    objects = PageManager()

    class Meta:
        ordering = ["flatpages__url"]
        order_with_respect_to = "parent"
        verbose_name = "page"
        verbose_name_plural = "pages"

    def __unicode__(self):
        return self.url

    class MPTTMeta:
        left_attr = "mptt_left"
        right_attr = "mptt_right"
        level_attr = "mptt_level"
        order_insertion_by = ["title"]

    def is_child_of(self, node):
        """
        Returns True if this is a child of the given node.
        """
        return (self.tree_id == node.tree_id and
            self.mptt_left > node.mptt_left and
            self.mptt_right < node.mptt_right)
