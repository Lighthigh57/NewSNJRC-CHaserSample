from Command import Command
import random


def main() -> None:
    runner = Command()  # サーバーと通信するためのインスタンス

    while True:
        value = runner.get_ready()  # サーバーに行動準備が完了したと伝える

        moved = True
        while moved:
            direction = random.randint(0, 3)
            if value[direction * 2 + 1] != 2:
                runner.move("walk", direction * 2 + 1)
                moved = False


if __name__ == "__main__":
    main()
