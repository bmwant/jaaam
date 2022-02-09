from rich._emoji_codes import EMOJI


def main():
    with open('emoji.md', 'w') as f:
        for em in EMOJI.keys():
            f.write(f':{em}: ')


if __name__ == '__main__':
    main()
