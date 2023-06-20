from textual.app import App
from textual.widgets import Header, Tree, Markdown
from textual.containers import Horizontal, VerticalScroll

from feedparser import parse
from markdownify import markdownify

blogs = [
    'https://www.pypy.org/rss.xml',
    'https://www.sqlalchemy.org/blog/feed/index.xml',
    'https://kdenlive.org/en/feed/',
    'https://pyfound.blogspot.com/feeds/posts/default',
]


def feed_parser():
    tree = Tree('Blogs', id='arvore')
    tree.styles.width = '30%'

    for blog in blogs:
        feed = parse(blog)
        tree_blogs = tree.root.add(feed['feed']['title'])

        for post in feed.entries[:4]:
            try:
                tree_blogs.add_leaf(
                    label=post.title,
                    data=post.content[0].value
                )
            except:
                tree_blogs.add_leaf(
                    label=post.title,
                    data=post.summary
                )

    return tree


class Feed(App):
    TITLE = 'Meu leitor de RSS!'

    def compose(self):
        yield Header(show_clock=True)
        with Horizontal():
            yield feed_parser()
            with VerticalScroll():
                yield Markdown(id='md')

    def on_tree_node_selected(self, event: Tree.NodeSelected):
        self.log('Entrei aqui!!!!')
        if event.node.data:
            element: Markdown = self.query_one('#md')
            element.action_scroll_home()
            element.update(
                f'# {event.node.label} \n {markdownify(event.node.data)}'
            )

Feed().run()
