class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False
    
    def has_child(self, char):
        return char in self.children

    def get_child(self, char):
        return self.children.get(char)
    
    def EndofWord(self, mark = None):
        if mark is not None:
            self.is_end_of_word = mark
        return self.is_end_of_word

class AutocompleteSystem:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        curr = self.root
        for char in word.lower():
            if not curr.has_child(char):
                curr.children[char] = TrieNode()
            curr = curr.get_child(char)
        curr.EndofWord(True)
    
    def search(self, prefix):
        curr = self.root
        
        for char in prefix.lower():
            if not curr.has_child(char):
                return None
            curr = curr.get_child(char)
        return curr

    def findwords(self, node, current_path, suggestions):
        if node.is_end_of_word:
            suggestions.append(current_path)
        
        for char in sorted(node.children.keys()):
            self.findwords(node.children[char], current_path + char, suggestions)


class main():
    def __init__(self):
        self.system = AutocompleteSystem()
    
    def user_input(self):
        return input("\nEnter prefix:").strip().lower()

    def suggestion(self, prefix):
        target_node = self.system.search(prefix)
        if target_node:
            results = []
            self.system.findwords(target_node, prefix, results)
            print(f"suggested words:{results}")
        else:
            print("cannot find prefix suggestion")

    def run_system(self):
        try: 
            with open("dictionary.txt", "r", encoding="utf-8") as file:
                for line in file:
                    word = line.strip()
                    if word: self.system.insert(word)
            print("Dictionary loaded!")
        
        except FileNotFoundError:
            print("Error: can't find dictionary.txt")
            return
        
        while True:
            prefix = self.user_input()
            if prefix == 'exit':
                print("Goodbye!")
                break
            if prefix:
                self.suggestion(prefix)

if __name__ == "__main__":
    app = main()
    app.run_system()