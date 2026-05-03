type PageMapItem = {
  name?: string;
  route?: string;
  title?: string;
  children?: PageMapItem[];
};

export type SearchItem = {
  title: string;
  route: string;
  breadcrumb: string;
};

export function buildSearchItems(pageMap: PageMapItem[]): SearchItem[] {
  const items: SearchItem[] = [];

  function visit(nodes: PageMapItem[], trail: string[]) {
    for (const node of nodes) {
      if (!node?.route || !node.title) {
        continue;
      }

      const nextTrail = [...trail, node.title];
      items.push({
        title: node.title,
        route: node.route,
        breadcrumb: nextTrail.join(' / '),
      });

      if (node.children?.length) {
        visit(node.children, nextTrail);
      }
    }
  }

  visit(pageMap, []);

  return items.filter((item, index, allItems) => {
    return allItems.findIndex((candidate) => candidate.route === item.route) === index;
  });
}