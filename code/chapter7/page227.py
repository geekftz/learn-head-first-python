from string import Template


def start_response(resp="text/html"):
    # 返回HTTP响应头，默认为text/html类型
    return ('Content-type: ' + resp + '\n\n')


def include_header(the_title):
    # 读取header模板文件，并用传入的标题替换模板变量
    with open('templates/header.html') as headf:
        head_text = headf.read()
    header = Template(head_text)
    return (header.substitute(title=the_title))


def include_footer(the_links):
    # 读取footer模板文件，并用传入的链接字典生成链接字符串替换模板变量
    with open('templates/footer.html') as footf:
        foot_text = footf.read()
    link_string = ''
    for key in the_links:
        link_string += '<a href="' + \
            the_links[key] + '">' + key + '</a>&nbsp;&nbsp;&nbsp;&nbsp;'
    footer = Template(foot_text)
    return (footer.substitute(links=link_string))


def start_form(the_url, form_type="POST"):
    # 返回form表单的起始标签，action为the_url，method默认为POST
    return ('<form action="' + the_url + '" method="' + form_type + '">')


def end_form(submit_msg="Submit"):
    # 返回form表单的结束标签和提交按钮，按钮文本默认为Submit
    return ('<p></p><input type=submit value="' + submit_msg + '"></form>')


def radio_button(rb_name, rb_value):
    # 返回一个单选按钮的HTML代码，name和value由参数指定
    return ('<input type="radio" name="' + rb_name +
            '" value="' + rb_value + '"> ' + rb_value + '<br />')


def u_list(items):
    # 根据传入的items列表生成无序列表的HTML代码
    u_string = '<ul>'
    for item in items:
        u_string += '<li>' + item + '</li>'
    u_string += '</ul>'
    return (u_string)


def header(header_text, header_level=2):
    # 返回指定级别的标题标签，默认为h2
    return ('<h' + str(header_level) + '>' + header_text +
            '</h' + str(header_level) + '>')


def para(para_text):
    # 返回一个段落标签，内容为para_text
    return ('<p>' + para_text + '</p>')


print(start_response())
print(start_response("text/plain"))

print(include_header("Welcome to my home on the web!"))
print(include_footer(
    {'Home': './index.html', 'Select': './cgi-bin/select.py'}))

print(include_footer({}))

print(start_form("./cgi-bin/process-attribute.py"))
print(end_form())

print(end_form("Click to Confirm Your Order"))

for fab in ['John', 'Paul', 'George', 'Ringo']:
    print(radio_button("fab", fab))

print(u_list(['Life of Brian', 'Holy Grail']))

print(header("Welcome to my home on the web!"))

print(header("This is a sub-sub-sub-sub heading", 5))

print(para("Was it worth the wait? We hope it was..."))
