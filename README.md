## Interview questions

Logic/algorithmic comments are contained in the individual scripts.

* Remove all spaces/whitespace from a string, (**rmwsp.py**) e.g.
		
		<python interpreter> rmwsp.py "This is a string with spaces."
	
			returns 
	
		string = "Thisisastringwithspaces."
	
* Find the longest common substring of two strings, (**lcsl.py**) e.g.

		<python interpreter> lcsl.py "This is a string" "a string"
		
			returns 

		longest common substring(s) = ['a string']
	
* Remove duplicate characters of a given string, (**rmdups.py**) e.g.

		<python interpreter> rmdups.py abca
		
			returns
			
		input string:		'abca         '
		unordered string:	'a cb'
		ordered string:	'abc '
	
* Reverse a singley-linked list, (**revlist.py**) e.g.

		<python interpreter> revlist.py a b c
		
			returns

		Original:	['a', 'b', 'c']
		Iterative:	['c', 'b', 'a']
		Recursive:	['c', 'b', 'a']
		
* Reverse a string, (**revstr.py**) e.g.

		<python interpreter> revstr.py this is a string
		
			returns
			
		Reversing as <class 'list'>

		Original:	['this', 'is', 'a', 'string']
		.reverse():	['string', 'a', 'is', 'this']
		In-place:	['string', 'a', 'is', 'this']
		for-loop:	['siht', 'si', 'a', 'gnirts']
		Slicing:	['string', 'a', 'is', 'this']
		
		Reversing as <class 'str'>
		
		Original:	this is a string
		Slicing:	gnirts a si siht
