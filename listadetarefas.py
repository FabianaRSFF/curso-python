"""
Faça uma lista de tarefas com as seguintes opções:
- Adicionar tarefa
- Listar tarefas
- Desfazer ( a cada vez que chamarmos desfaz uma opção)
- Refazer ( a cada vez que chamarmos refaz uma opção)
"""


def show_op(todo_list):
    print()
    print('tarefas: ')
    print(todo_list)
    print()


def do_undo(todo_list, redo_list):
    if not todo_list:
        print('Nada a desfazer.')
        return
    last_todo = todo_list.pop()
    redo_list.append(last_todo)


def do_redo(todo_list, redo_list):
    if not redo_list:
        print('Nada a refazer.')
        return
    last_redo = redo_list.pop()
    todo_list.append(last_redo)


def do_add(todo, todo_list):
    todo_list.append(todo)


if __name__ == '__main__':
    todo_list = []
    redo_list = []

    while True:
        todo = input('Digite uma tarefa, ou undo, redo, ls: ')
        if todo == 'ls':
            show_op(todo_list)
            continue
        elif todo == 'undo':
            do_undo(todo_list, redo_list)
            continue
        elif todo == 'redo':
            do_redo(todo_list, redo_list)
            continue

        do_add(todo, todo_list)