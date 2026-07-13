'''
###AI Workflow 
types
1) linear pipeline

input -> step1(AI) -> step2(AI) -> step3(Save) -> done

2)branching workflow
 input -> AI_Classify -> if 'urgent': send_alert()
                         if 'routine': add_to_queue()
                         if 'spam': delete()

3)looping workflow
 - process a list item one by one
    for students in student_list:
        report = ai_generate_report(student)
        save_report(report)

4)scheduled workflow:-
- runs at a specific time or interval
   import schedule, time
   def news():
    #news fetching code -> AI_Summarize -> email()
   schedule.every().day.at("08:00").do(news)
   while True:
    schedule.run_pending()
    time.sleep(1)




'''