import textwrap

def wrap(string, max_width):
    my_wrap = textwrap.TextWrapper(width=max_width)
    wraped_list = my_wrap.wrap(text=string)
    x = ("\n".join(wraped_list))
    return x

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)