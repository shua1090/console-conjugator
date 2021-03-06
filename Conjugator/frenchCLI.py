import argparse
import platform

from Conjugator.Francaisconjugation import conjugator
from Conjugator.Francaisconjugation.__version__ import __version__

def get_args() -> str:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "mode",
        nargs=1,
        choices=["c", "v"],
        help="The conjugation functions that can be performed (c -> conjugate, v -> version).",
    )
    current_mode = vars(parser.parse_known_args()[0])["mode"]
    if "c" in current_mode:
        parser.add_argument(
            "infinitive",
            nargs=1,
            help="infinitive: The infinitive of the verb.",
        )
        parser.add_argument(
            "pronoun",
            nargs=1,
            help="pronoun: The pronoun to be conjugated for. 'es' is not \
                    currently supported (use 'er' instead).",
        )
        parser.add_argument(
            "tense",
            nargs=1,
            help="tense: The tense to be conjugated for. Only indikativ tenses, \
                not including Futur II or Imperative (to be added soon)",
        )
    elif "v" in current_mode:
        print(f"Francais-Conjugation version v{__version__}")
    else:
        raise argparse.ArgumentError(
            "You did not provide a proper mode (f, c, or a), please try again with one of such arguments",
        )
    args = parser.parse_args()
    return args


# Lower_case the args
def lower_format() -> (str, str, str):
    args = get_args()
    return args.infinitive[0].lower(), args.pronoun[0].lower(), args.tense[0].lower()


def mode_selection():
    args = get_args()
    if args.mode[0] == "c":
        infinitive, pronoun, tense = lower_format()
        z = conjugator.conjugate(infinitive, pronoun, tense)
        print(z)
    # if args.mode[0] == "a":
    #     args = get_args()
    #     conjugator.allConjugate(
    #         args.infinitive[0], [args.tense[0]], getColorAvailability()
    #     )


def main():
    mode_selection()


if __name__ == "__main__":
    main()
