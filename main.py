import argparse,login,gui

if __name__ == '__main__' :
    parser = argparse.ArgumentParser(description='ruijie')
    parser.add_argument('--userId','-u')
    parser.add_argument('--encryptedPassword','-e')
    args = parser.parse_args()
    if args.userId is not None :
        try:
         login.login(args.userId,args.encryptedPassword)
        except Exception as e:
         pass
    else:
        gui.gui()