from secrets import token_urlsafe

END_PARTICLE = "END"  # The particle that should end the tape.


def generate_tape(length=20):
    tape = token_urlsafe(length)
    tape += END_PARTICLE
    return tape
