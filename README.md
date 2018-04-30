# custom-tree-data-structure-part-of-educational-tool

This is a story/game created with python and pygame to teach, in a light-hearted, fun way, middle school students some of the possibilities they have with if-statements.
The story unfolds by branching out with each of the user's choice. Dictionaries, .txt files, .json files and databases were used with unique ids following a specific pattern that is used to recognized a node's branches

txt Format: node name\tnumber of children\tvalue\tparent node\tchild1\tchild2\tchildN\tbutton1 text\t button2 text\t buttonN text\t is first\t is last

json format: "block":{
		"id": "block",
		"children":
			["child1id", "child2id", "childnid],
		"parent": "parentid",
		"isFinal": bool,
		"isStarting": bool,
		"text": "Your desired value",
		"buttonText": ["text1", "text2", "textn"]
	}



![data](https://user-images.githubusercontent.com/38569768/39427839-e909b96c-4c8d-11e8-97e7-08e29b92fcd1.png)

![start_menu](https://user-images.githubusercontent.com/38569768/39070519-674c9a6e-44ec-11e8-81e3-75a26bb26812.png)

![role_selection](https://user-images.githubusercontent.com/38569768/39070599-ab8a9078-44ec-11e8-92ea-8caeef8c673f.png)

![choose_path](https://user-images.githubusercontent.com/38569768/39070649-d4c42d32-44ec-11e8-99b3-37ec14eaa8b0.png)
