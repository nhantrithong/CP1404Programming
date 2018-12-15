#done

from prac_06.programming_language import ProgrammingLanguage

def main():
    list = []
    list2 = []
    ruby = ProgrammingLanguage("Ruby", "Dynamic", True,1995)
    list.append(ruby)
    python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
    list.append(python)
    visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, 1991)
    list.append(visual_basic)
    #print("{}, {}, Reflection = {}, First appeared in {}".format(ruby.name, ruby.typing, ruby.reflection, ruby.year))
    #print("{}, {}, Reflection = {}, First appeared in {}".format(python.name, python.typing, python.reflection, python.year))
    #print("{}, {}, Reflection = {}, First appeared in {}".format(visual_basic.name, visual_basic.typing, visual_basic.reflection, visual_basic.year))
    print(ruby)
    print(python)
    print(visual_basic)

    for language in list:
        if language.is_dynamic() == True:
            list2.append(language.name)
    print("The dynamically typed languages are:")
    for i in list2:
        print(i)


main()