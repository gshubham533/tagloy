def trblsht():


    ans = {}

    ans['1'] = "My content is not displayed."
    ans['2'] = "My live box is not working properly."
    ans['3'] = "Unable to upload picture/video "
    ans['4'] = "what"
    ans['5'] = "End"

    while False:
        options = ans.keys()
        print(options)

        for entry in options:
            print("entry, ans[entry]")




    while ans:

        ans=input("""Welcome to the Troubleshoot menu! \n 1.My content is not displayed \n 2.My live box is not working properly \n 3.Unable to upload picture/video \n 4.next question \n 5.last que
        """)
        if ans == "1":
          print("\n your problem is solved and content is diplayed \n")
        elif ans == "2":
          print("\n live box is working properly \n ")
        elif ans == "3":
          print("\n sucessfully uploaded \n")
        elif ans == "4":
          print("\n next...... \n")
        elif ans == "5":
          print("\n exit......\n")
trblsht()