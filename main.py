import random
import subprocess
import sys

def generate_random_input(config): # 각 문제 입력 조건에 맞는 난수 생성 코드 입력
    N = random.randint(1, config.get("max_N", 100))
    input_str = f"{N}\n"

    for _ in range(N):
        A = random.randint(0, config.get("max_A", 1000))
        B = random.randint(0, config.get("max_B", 1000))
        input_str += f"{A} {B}\n"

    return input_str.strip()


def run_code(filename, input_data):
    result = subprocess.run([sys.executable, filename], input=input_data, text=True, capture_output=True)
    return result.stdout.strip()


def find_counterexample(correct_file, incorrect_file, config, num_tests):
    for i in range(num_tests):
        input_data = generate_random_input(config)
        correct_output = run_code(correct_file, input_data)
        incorrect_output = run_code(incorrect_file, input_data)

        if correct_output != incorrect_output:
            print(f"반례를 찾았습니다! (case #{i + 1}):")
            print(f"입력:\n{input_data}")
            print(f"정답 출력:\n{correct_output}")
            print(f"오답 출력:\n{incorrect_output}")
            return True

    print(f"{num_tests}개의 테스트 케이스에서 반례를 찾지 못했습니다.")
    return False


if __name__ == "__main__":
    correct_file = "correct.py"
    incorrect_file = "incorrect.py"

    config = {
        "max_N": 100,
        "max_A": 1000,
        "max_B": 1000
    }

    num_tests = 1000  # 테스트 횟수

    find_counterexample(correct_file, incorrect_file, config, num_tests)

# BOJ 25377 예시
# 반례를 찾았습니다! (case #1):
# 입력:
# 35
# 36 371
# 52 391
# 858 110
# 537 970
# 300 326
# 956 747
# 202 458
# 875 634
# 857 595
# 201 818
# 300 138
# 903 606
# 504 901
# 434 459
# 595 812
# 343 129
# 977 124
# 584 426
# 98 354
# 465 753
# 944 853
# 97 216
# 136 463
# 336 320
# 795 667
# 887 120
# 531 993
# 185 975
# 372 620
# 407 98
# 912 524
# 649 530
# 263 229
# 716 784
# 61 523
# 정답 출력:
# 216
# 오답 출력:
# 459