import os
from colorama import init, Fore, Style
init(autoreset=True)

def extract_invoice_data(file_path):
    data = {}
    with open(file_path, 'r') as file:
        for line in file:
            if "Invoice Number" in line:
                data['invoice_number'] = line.strip().split(":")[1].strip()
            elif "Date" in line:
                data['date'] = line.strip().split(":")[1].strip()
            elif "Client" in line:
                data['client'] = line.strip().split(":")[1].strip()
            elif "Amount" in line:
                data['amount'] = float(line.strip().split(":")[1].strip())
    return data

def save_summary_to_file(data_list, total_invoices, total_amount, output_file="summary.txt"):
            with open(output_file, 'w') as file:
                file.write("Invoice Summary Report\n")
                file.write("=======================\n\n")
                file.write(f"{'Invoice':<12} | {'Client':<25} | {'Amount (KES)':>15}\n")
                file.write("-" * 56 + "\n")

                for invoice in data_list:
                    file.write(f"{invoice['invoice_number']:<12} | {invoice['client']:<25} | {invoice['amount']:>15,.0f}\n")

                file.write("\n" + "-" * 56 + "\n")
                file.write(f"{'TOTAL':<12} | {'':<25} | {total_amount:>15,.0f}\n")
                file.write(f"{'Total Invoices:':<20} {total_invoices}\n")

def main():
    folder = "invoices"
    total_amount = 0
    invoice_count = 0
    all_data = []

    print(Fore.CYAN + "Reading invoice files...\n")

    for filename in os.listdir(folder):
        if filename.endswith(".txt"):
            filepath = os.path.join(folder, filename)
            invoice = extract_invoice_data(filepath)
            all_data.append(invoice)
            invoice_count += 1
            total_amount += invoice['amount']
            print(Fore.GREEN + f"✓ {invoice['invoice_number']} | {invoice['client']} | KES {invoice['amount']:,}")

    print(Fore.YELLOW + "\n--- Summary ---")
    print(Fore.YELLOW + f"Total Invoices: {invoice_count}")
    print(Fore.YELLOW + f"Total Amount: KES {total_amount:,}")

    print(Fore.MAGENTA + "Summary saved to summary.txt")


if __name__ == "__main__":
    main()
