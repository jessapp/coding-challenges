# Implement a trie

class Trie:

    def __init__(self):
        self.root = {}

    def check_present_and_add(self, word):
        
        current_node = self.root

        is_new_word = False

        # Goes through the trie, adding nodes as needed

        for char in word:
            if char not in current_node:
                is_new_word = True
                current_node[char] = {}
            current_node = current_node[char]

        print current_node

        # Explicitly mark the end of the word 
        
        if "End Of Word" not in current_node:
            is_new_word = True
            current_node['End Of Word'] = {}

        print current_node

        return is_new_word