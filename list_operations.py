

def insert_into_list():
    self._memory = [
            *self._memory[:self._pointer],
            *insert,
            *self._memory[self._pointer+len(insert):]
        ]
