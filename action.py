import subprocess

if __name__ == '__main__':
    ls_output = subprocess.check_output(['ls', '-l'])
    print(ls_output)
    print(f'Test action')