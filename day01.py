# 교재 딕셔너리 예제

subjects = {
    '의사소통 영어' : 'A+',
    '오래된 미래' : 'B+',
    '양자역학' : 'A0',
    }
student = '김도훈'
subject = '오래된 미래'
print(student, '학생의', subject, '과목 성적은', subjects[subject], '입니다' )
# old style
print("%s 학생의 %s 과목 성적은 %s입니다" % (student, subject, subjects[subject]))
# modern style (format 함수)
print("{} 학생의 {} 과목 성적은 {}입니다".format(student, subject, subjects[subject]))
# ultra modern style (f스트링)
print(f'{student} 학생의 {subject} 과목 성적은 {subjects[subject]}입니다')
