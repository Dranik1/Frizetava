#iznemumi

def divide_num():
    try:
        num1=float(input("Ievadiet pirmo skaitli: "))
        num2=float(input("Ievadiet otro skaitli: "))
        res=num1/num2
        print(f'Rezultats {res}')
    
    except ZeroDivisionError:
        print("Nedrīkst dalit uz nilli")

    except ValueError:
        print("Ievadietie skaitli nav pareizi")

    except Exception as e:
        print(e)

    finally:
        print("Darbība ir pabeigta")