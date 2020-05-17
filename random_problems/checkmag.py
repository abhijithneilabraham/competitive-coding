def checkMagazine(magazine, note):

    for i in note:
        if  note.count(i)>magazine.count(i) or i not in magazine:
            print("No")
            return "No"
    print("Yes")
    return "Yes"