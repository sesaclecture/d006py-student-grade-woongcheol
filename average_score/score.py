#!/usr/bin/env python
import sys
import csv


def load_from_csv(filepath):
    """
    Read students' names and scores from given 
    csv file and return it in dict with list of subjects.
    """
    student_scores = {}

    with open(filepath, 'r', encoding='utf-8') as f:
        csv_reader = csv.reader(f)

        # Readout the header
        # 이름, 국어, 수학, 영어, 과학, 사회
        header = next(csv_reader)

        for row in csv_reader:
            student_scores[row[0]] = row[1:]
    return student_scores, header[1:]


def subject_average(student_scores: dict, subjects: list):
    """
    이 반의 각 과목별 평균을 구해서 딕셔너리로 반환
    예) {"국어": 80.8, "수학": 35.3, "영어": 96.6, "과학": 85.3, "사회": 38.8}
    """
    subject_scores = {}
    for student_score in student_scores:
        for i, score in enumerate(student_scores[student_score]):
            if subjects[i] not in subject_scores:
                subject_scores[subjects[i]] = int(score)
            else:
                subject_scores[subjects[i]] += int(score)
    
    for sum_score in subject_scores:
        subject_scores[sum_score] /= len(student_scores) 

    return subject_scores


def student_average(student_scores: dict):
    """
    각 학생별 전과목 평균 점수를 정렬된 튜플의 리스트로 반환
    예) [("이영희", 89.8), ("김철수", 86.6), ("박민수", 84.8)]
    """
    
    student_avg = []
    for student, student_score in student_scores.items():
        sum_score = 0

        for score in student_score:
            sum_score += int(score)

        student_avg.append((student, sum_score/len(student_score)))

    student_avg.sort(key=lambda x: x[1], reverse=True)
    
    return student_avg
            
if __name__ == "__main__":
    if len(sys.argv) < 2:
        print(f"USAGE: {sys.argv[1]} <csv_file>")
        sys.exit()

    student_scores, subjects = load_from_csv(sys.argv[1])
    sub_avg = subject_average(student_scores, subjects)

    stud_avg = student_average(student_scores)

    print("과목 평균:")
    for sub, avg in sub_avg.items():
        print(f"\t{sub}: {avg:.2f}")

    print("학생 점수:")
    for avg in stud_avg:
        print(f"\t{avg[0]}: {avg[1]:.2f}")
