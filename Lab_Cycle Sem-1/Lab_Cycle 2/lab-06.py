import pandas as pd 

df=pd.read_csv("Lab_Cycle Sem-1\Lab_Cycle 2\student-scores.csv")

df_cleaned = df.drop_duplicates()

marks=['math_score','history_score','physics_score','chemistry_score','biology_score','english_score','geography_score']

for col in marks:
    df[col] = df[col].fillna(df[col].median())

print(f"✓ Cleaned dataset: {df.shape[0]} rows, {df.shape[1]} columns")
print(f"✓ Missing values: {df.isnull().sum().sum()}")   

print("\nTop Students by Subject:")

for col in marks:
    subject = col.replace('_score', '').title()
    max_idx = df[col].idxmax()
    student = df.loc[max_idx]
    print(f"  {subject:12s}: {student['first_name']} {student['last_name']} - {student[col]} marks")

print("\nAverage Marks by Grade:")

df['average_score'] = df[marks].mean(axis=1)

def assign_grade(score):
    if score >= 90: return 'A'
    elif score >= 80: return 'B'
    elif score >= 70: return 'C'
    elif score >= 60: return 'D'
    else: return 'F'

df['grade'] = df['average_score'].apply(assign_grade)

grade_avg = df.groupby('grade')['average_score'].agg(['mean', 'count']).round(2)
grade_avg.columns = ['Average_Marks', 'Student_Count']

print(grade_avg.sort_values('Average_Marks', ascending=False))