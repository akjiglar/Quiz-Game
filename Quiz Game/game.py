from PyInquirer import style_from_dict, prompt,Token, Separator

style = style_from_dict({
	Token.Separator : '#fff',      #white
	Token.QuestionMark : '#000',   #black
	Token.Selected : '#00BFFF',    #sky blue
	Token.Pointer : '#fff',        #white
	Token.Instruction : '#fff',    #white
	Token.Answer : '#008000 bold', #green
	Token.Question : '#FF7F50',    #shade of orange
})

questions = [
				{
					'type' : 'list',
					'name' : 'capital',
					'message' : '1. What is capital of Russia ?',
					'choices' : ['Tokyo','Beijing','Ontario','Moscow'],
				},
				{
					'type' : 'list',
					'name' : 'currency',
					'message' : '2. What is currency of China ?',
					'choices' : ['Dollars','Yen','Yuan','Krone']
				},
				{
					'type' : 'list',
					'name' : 'animal',
					'message' : '3. What is National Animal of India ?',
					'choices' : ['Tiger','Lion','Leopard','Panther']
				},
				{
					'type' : 'list',
					'name' : 'kb',
					'message' : '4. 1 KB in bytes is equal to ?',
					'choices' : ['1000','1032','1024','1098']
				},
				{
					'type' : 'list',
					'name' : 'continent',
					'message' : '5. Largest Continent on Earth ?',
					'choices' : ['Australia','Asia','Antarctica','Africa']
				}
			]

def main():
	answers = prompt(questions,style = style)
	return answers
