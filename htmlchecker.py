# Write a program that can check an HTML document for proper opening and closing tags.

def check_html(html_str):

    closers_and_openers = {
                            "</html>": "<html>",
                            "</head>": "<head>",
                            "</title": "<title>",
                            "</body>": "<body>"
                            }

    stack = []

    words = html_str.split()

    for word in words:
        if word in closers_and_openers.values():
            stack.append(word)
        elif word in closers_and_openers:
            if stack[-1] == closers_and_openers[word]:
                stack.pop()
            else:
                return False

    if stack == []:
        return True
    else:
        return False

# future challenge: make a class, and build dict with HTML openers you encounter 