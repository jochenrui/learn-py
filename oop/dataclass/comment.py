from dataclasses import dataclass


@dataclass(frozen=True, order=True)
class Comment:
    id: int
    text: str


def main():
    comment = Comment(1, "I just subscribed")
    print(comment)


if __name__ == '__main__':
    main()
