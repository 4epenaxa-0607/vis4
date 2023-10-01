import sys
import random
import sqlite3

def initialize_database():
    conn = sqlite3.connect('results.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS results
                 (name text, result integer)''')
    conn.commit()
    conn.close()


def generate_example():
    """Генерирует случайный пример"""
    a = random.randint(1, 100)
    b = random.randint(1, 100)
    operator = random.choice(['+', '-'])
    example = f"{a} {operator} {b}"
    return example

def solve_example(example):
    """Решает пример и возвращает результат"""   
    result = eval(example)
    return result
    
def display_leaderboard():
    conn = sqlite3.connect('results.db')
    c = conn.cursor()
    
    c.execute("SELECT name, result FROM results ORDER BY result DESC")
    rows = cursor.fetchall()
        
    print("Таблица лидеров:")
    for row in rows:
    	print(row)
    
    conn.close()

    
def main():
    initialize_database()
    conn = sqlite3.connect('results.db')
    c = conn.cursor()
    
    name = input("Введите ваше имя: ")
    x = 0
    
    while True:
        example = generate_example()
        print(f"Решите пример: {example}")
        user_answer = input("Введите ваш ответ (или 'q' для выхода): ")
        
        if user_answer.lower() == 'q':
            c.execute("INSERT INTO results VALUES (?, ?)", (name, x))
            conn.commit()
            c.execute("SELECT name, result FROM results ORDER BY result DESC")
            rows = c.fetchall()
        
            print("Таблица лидеров:")
            for row in rows:
                print(row)
    
            conn.close()
            break
        
        correct_answer = solve_example(example)
        
        if str(correct_answer) == user_answer:
            x = x + 1
            print(f"Правильно! У вас {x} очков!")
        else:
            c.execute("INSERT INTO results VALUES (?, ?)", (name, x))
            conn.commit()
            c.execute("SELECT name, result FROM results ORDER BY result DESC")
            rows = c.fetchall()
            
            print("Таблица лидеров:")
            for row in rows:
                print(row)
    
            conn.close()
            
            print(f"Неправильно. Правильный ответ: {correct_answer}")
            break
        
        # Store the name and result in the database
        
        
        print()

if __name__ == "__main__":
    main()


