class Tree:
  def __init__(self, root = None):
    self.root = root

  def get_element_by_id(self, id):
    result = []
    nodes_to_visit = [self.root]

    while len(nodes_to_visit) > 0:
      
      # 1. Remove the first node from the `nodes_to_visit` list
      self.root = nodes_to_visit.pop(0)
    
      if self.root['id'] == id:

        # 2. Add its value to the result list
        result.append(self.root)

      # 3. Add its children (if any) to the BEGINNING of the `nodes_to_visit` list
      nodes_to_visit = self.root['children'] + nodes_to_visit

    return result[0] if result else None