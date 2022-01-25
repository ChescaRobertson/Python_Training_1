file_contents = """
1234,smith     ,500.0
2345,jones     ,-150.0
3456,wilson    ,2000.0
4567,thompson  ,275.0
5678,davis     ,100
"""

accounts = {}

lines = file_contents.splitlines()

for line in lines:
    if line:
        parts = line.split(',')
        acc_num = int(parts[0])
        acc_name = parts[1].strip().title()
        acc_balance = float(parts[2])

        accounts[acc_num] = {
            "number": acc_num,
            "name": acc_name,
            "balance": acc_balance
            }

for acc_num in accounts:
    print(accounts[acc_num])
