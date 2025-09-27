class BufferFullException(BufferError):
    """Exception raised when CircularBuffer is full.

    message: explanation of the error.

    """

    def __init__(self, message: str):
        super().__init__(message)


class BufferEmptyException(BufferError):
    """Exception raised when CircularBuffer is empty.

    message: explanation of the error.

    """

    def __init__(self, message: str):
        super().__init__(message)


class CircularBuffer:
    """
    A circular buffer (ring buffer) is a fixed-size data structure that wraps around when the end is reached.

    It supports reading, writing, overwriting, and clearing operations. When full, writing raises BufferFullException;
    when empty, reading raises BufferEmptyException.
    """

    def __init__(self, capacity: int):
        """
        Initialize a new CircularBuffer with a given capacity.

        Args:
            capacity (int): The maximum number of bytes the buffer can hold.
        """
        self.capacity = capacity
        self.clear()

    def _advance_read(self) -> None:
        """
        Advance the read index to the next position, wrapping around if necessary.
        """
        self.read_idx = (self.read_idx + 1) % self.capacity
        self.count -= 1

    def read(self) -> str:
        """
        Read and remove the oldest element from the buffer.

        Returns:
            The oldest element in the buffer (as a string).

        Raises:
            BufferEmptyException: If the buffer is empty.
        """
        if self.count == 0:
            raise BufferEmptyException("Circular buffer is empty")

        value = chr(self.buffer[self.read_idx])
        self._advance_read()

        return value

    def write(self, data: str) -> None:
        """
        Write a string (single character) to the buffer at the current write position.

        Args:
            data (str): The data to write (must be a single character string).

        Raises:
            BufferFullException: If the buffer is full.
        """
        if self.count == self.capacity:
            raise BufferFullException("Circular buffer is full")

        self._write(data)

    def overwrite(self, data: str) -> None:
        """
        Overwrite the oldest data in the buffer with new data if the buffer is full.

        Args:
            data (str): The data to write (must be a single character string).
        """
        if self.count == self.capacity:
            self._advance_read()

        self._write(data)

    def _write(self, data: str) -> None:
        """
        Internal helper to write a string (single character) at the current write index and advance the write index.

        Args:
            data (str): The data to write (must be a single character string).
        """
        if len(data) != 1:
            raise ValueError("data must be a single character string")

        self.buffer[self.write_idx] = ord(data)

        # Advance the write index to the next position, wrapping around if necessary.
        self.write_idx = (self.write_idx + 1) % self.capacity
        self.count += 1

    def clear(self) -> None:
        """
        Clear the buffer, removing all elements and resetting indices.
        """
        self.write_idx = 0
        self.read_idx = 0
        self.count = 0
        self.buffer = bytearray(self.capacity)
