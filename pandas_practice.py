import pandas as pd

employee = pd.DataFrame({'id': [1,2,3], 'salary': [0,0,1]})  # Replace with your data

def second_highest_salary(employee: pd.DataFrame) -> pd.DataFrame:
    salaries_ranked = employee['salary'].rank(method='dense',ascending=False)
    df_temp = pd.DataFrame({'salary': employee['salary'], 'rank': salaries_ranked})
    sorted_df = df_temp.sort_values(by=['rank', 'salary'], ascending=[True, False])
      # Check if there are at least 2 unique salary values
    if len(sorted_df) >= 2 and len(sorted_df['rank'].unique()) >= 2:
    # Get the second element (considering ties)
        second_highest_salary = sorted_df[sorted_df['rank'] == 2][['salary']]
        second_highest_salary.columns = ['SecondHighestSalary']
        second_highest_salary= second_highest_salary.drop_duplicates()
    else:
    # No second highest salary, create DataFrame with None
        second_highest_salary = pd.DataFrame(columns=['SecondHighestSalary'])
        second_highest_salary.loc[0, 'SecondHighestSalary'] = None
    return second_highest_salary

print(second_highest_salary(employee))