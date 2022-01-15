# STACK
The analogy of this data structure is :
We have 4 books spread all over the place.We decided to keep it neatly at on place. The best way to put the books at one place is by putting it on top of each other. Now we have a nice stack of books! 
 If we want to retrieve a book from this stack, we can take the book on top. Taking a book from the bottom is a bit precarious and we don’t want to topple the entire stack. 
 Therefore, we’ll take down the top book on the stack and read it or do whatever we want to do with it.
 Let’s say we want to take Book A. Right now, it is at the bottom of the stack, so we need to take Book D, put it down, then do the same for Book C and Book B, and then we can access Book A.
 This is the idea of stack. The data structure stack is very similar to our book stack.

 # Stack Operation
 There are mainly 3 stack operation
 push()- This operation insert element in stack. When we push the book on a stack, we put the book on the top element which means now this book is the top element.

 pop()-There is another operation that we can perform on the stack, popping. Popping is when we take the top book of the stack and put it down. This implies that when we remove an element from the stack, the stack follows the First-In, Last Out property. This means that the top element, the last to be inserted, is removed when we perform the pop operation.
 Push and Pop are two fundamental routines that we’ll need for this data structure.

 peek()-Another thing that we can do is view the top element of the stack so we can ask the data structure: “What’s the top element?” and it can give that to us using the peek operation. Note that the peek operation does not remove the top element, it merely returns it.