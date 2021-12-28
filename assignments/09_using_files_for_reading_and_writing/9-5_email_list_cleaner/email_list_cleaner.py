"""Email list cleaner program."""

from csv import reader, writer

def main():
    """Formats anmes and removes whitspace from an email list csv."""
    print('Welcome to the Email List Cleaner\n')
    email_list_target: str = input('Source list: ')
    cleaned_email_list_target: str = input('Cleaned list: ')
    email_list: list[list[str]] = read_sales_file(email_list_target)
    cleaned_email_list = clean_email_list(email_list)
    save_cleaned_to_csv(cleaned_email_list_target, cleaned_email_list)

def clean_email_list(email_list: list[list[str]]) -> list[list[str]]:
    """Clean the email list by formating all names to title case and email addresses to lowercase."""
    cleaned_email_list: list[list[str]] = []
    for row in email_list:
        if row != email_list[0]:
            cleaned_email_list.append([row[0].title().strip(), row[1].title().strip(), row[2].lower().strip()])
    return cleaned_email_list

def read_sales_file(target_file: str):
    """Read the target sales csv file."""
    with open(target_file, encoding='utf-8') as target_file:
        csv = reader(target_file)
        return [row for row in csv]

def save_cleaned_to_csv(target_file: str, content: list[list[str]]) -> None:
    """Write cleaned csv data to target csv file."""
    with open(target_file, 'w', newline='', encoding='utf-8') as target_file:
        csv = writer(target_file)
        csv.writerows(content)

if __name__ == '__main__':
    main()