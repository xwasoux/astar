def wait_until_finished(self):
        """
        Waits until all processors are finished processing.

        The method iterates through the processors and waits for each one to finish.
        It uses a small sleep duration between checks to avoid unnecessary resource consumption.
        """
        for file_path, processor in self._processors.items():
            while not processor.done:
                time.sleep(0.1)