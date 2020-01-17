from all_pb2 import User

if __name__ == '__main__':
    user = User()
    user.id = 'test_user'
    user.name = 'iamuser'

    print('this is what i will to log in the message console:')
    print(str(user))
    print('set a breakpoint on this line to watch the variable `user`')
    pass
