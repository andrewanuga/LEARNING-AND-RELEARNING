def main():
    starting_data = [5, 10, 4, 30, 5]
    my_stack = Stack(starting_data)
    
    # We use a list to collect results so we can see everything at the end
    results = []
    
    results.append(f"Peek: {my_stack.peek()}")      # Should look at the last 5
    results.append(my_stack.push(99))               # Pushes 99 to the top
    results.append(f"Pop: {my_stack.pop()}")        # Pops 99 back off
    results.append(f"Is Empty? {my_stack.isEmpty()}") 
    
    return results

class Stack:
    def __init__(self, initial_list):
        self.lists = list(initial_list) if initial_list else []

    def push(self, item):
        self.lists.append(item)
        return f"pushed {item}"
    
    def pop(self):
        return self.lists.pop() if not self.isEmpty else "Stack Underflow"
    
    def peek(self):
        return self.lists[-1] if not self.isEmpty else "Stack Underflow"
    
    def isEmpty(self):
        return len(self.lists) == 0
    
print(main())