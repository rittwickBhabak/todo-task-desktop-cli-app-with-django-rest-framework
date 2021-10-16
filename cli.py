import requests, json, datetime 

def main():
    BASE_URL  = "http://127.0.0.1:8081/api/todos"
    AUTH_DATA = ('rittwick', 'rittwick')

    def create(input_data):
        res = requests.post(f'{BASE_URL}/create', auth=AUTH_DATA, data=input_data)
        return res 

    def update(input_data, id):
        res = requests.put(f'{BASE_URL}/{id}/update', auth=AUTH_DATA, data=input_data)
        return res

    def get(id):
        res = requests.get(f'{BASE_URL}/{id}', auth=AUTH_DATA)
        return res 

    def delete(id):
        res = requests.delete(f'{BASE_URL}/{id}/delete', auth=AUTH_DATA)
        return res

    def get_all():
        res = requests.get(f'{BASE_URL}', auth=AUTH_DATA)
        return res 

    def get_status(status):
        if not status:
            return 'Not Done'
        else:
            return 'Done'
    while True:
        print('\n-------------------------------------------------------------')
        all_todos = json.loads(get_all().text)
        if len(all_todos)>0:
            for index, todo in enumerate(all_todos):
                print(f"{todo['id']:3}: {get_status(todo['is_completed']) }...{todo['title']} ")
            print('-------------------------------------------------------------')
            print('a. Choose a todo (enter it\'s slno)')
        else:
            print('----------------------------------------')
            print('No task is available.')
            print('----------------------------------------')

        print('b. Create new todo')
        print('c. Exit')
        user_input = input('Enter Choice: ')
        if user_input.lower() == 'b':
            print('--------------------------')
            title = input('Enter todo name: ')
            res = create({'title': title})
            if res.status_code == 201:
                print('--------------------------')
                print('Todo created successfully.')
                print('--------------------------')
                input('Press enter to go to main menu.')
            else:
                print('------------------------------------------')
                print('Failed to create todo. Some error occoured')
                print('------------------------------------------')
                input('Press enter to go to main menu')
        elif user_input.lower() == 'c':
            exit()
        else:
            try:
                slno = int(user_input)
                res = get(slno)
                if res.status_code == 200:
                    todo = json.loads(res.text)
                    print("\n---------------------------------------------------")
                    print(f'Task: {todo["title"]}')
                    if todo['is_completed']:
                        print('The task is completed')
                    else:
                        print('The task is not completed till now')
                    print(f"Created at: {' '.join(todo['created_at'][:10].split('-'))}")
                    print('----------------------------------------------------')
                    print('1. Is the task completed?')
                    print('2. The task is completed and want to delete it?')
                    print('3. Delete this task?')
                    print('4. Go back to main menu')
                    print('5. Exit')
                    user_input = input('Enter your choice: ')
                    while user_input not in ['1','2','3','4', '5']:
                        user_input = input('Enter a valid choice: ')
                    if user_input=='1':
                        res = update({'title':todo['title'], 'is_completed': True}, todo['id'])
                        if res.status_code==200:
                            print("---------------------------------------------------")
                            print('Congratulations! You have completed the task!')
                            print("---------------------------------------------------")
                            input('Press enter to go to main menu')
                        else:
                            print("---------------------------------------------------")
                            print('Some error occoured. Failed to Update. Any way congratulations for completing the task.')
                            print("---------------------------------------------------")
                    elif user_input=='2' or user_input=='3':
                        res = delete(todo['id'])
                        if res.status_code==204:
                            print("---------------------------------------------------")
                            print('The task is deleted successfully')
                            print("---------------------------------------------------")
                            input('Press enter to go to main menu.')
                        else:
                            print("---------------------------------------------------")
                            print('Some error occoured. Failed to delete the task')
                            input('Press enter to go to main menu.')
                            print("---------------------------------------------------")
                    elif user_input=='4':
                        pass 
                    else:
                        exit()
                else:
                    print('The task do not exist!')
            except Exception as e:
                print(str(e))
                print('Enter a valid input.')


        

if __name__=="__main__":
    main()
