"""Calculate the gross pay, tax amount, and net pay based hours worked and pay rate."""

def main() -> None:
    """Take worker input and provide gross pay, tax rate, tax amount, and take-home pay to worker."""
    print('Pay Check Calculator\n')

    TAX_RATE: int = 18
    hours: float = float(input('Hours Worked:\t '))
    pay_rate: float = float(input('Hourly Pay Rate: '))
    
    gross_pay: float = round(hours * pay_rate, 2)
    tax_amount: float = round(gross_pay * (TAX_RATE/100), 2)
    net_pay: float = round(gross_pay - tax_amount, 2)

    print(f'\nGross Pay:\t {gross_pay}')
    print(f'Tax Rate:\t {TAX_RATE}%')
    print(f'Tax Amount:\t {tax_amount}')
    print(f'Take Home Pay:\t {net_pay}')


if __name__ == '__main__':
    main()

