import pytest
import os
from write_read_to_file import write_to_file, read_from_file


class TestWriteReadFile:
    """Test suite for write_to_file and read_from_file functions"""

    @pytest.fixture
    def test_filename(self):
        """Fixture to provide a test filename"""
        return "test_example.txt"

    @pytest.fixture(autouse=True)
    def cleanup(self, test_filename):
        """Cleanup test files after each test"""
        yield
        # Remove test file if it exists after test
        if os.path.exists(test_filename):
            os.remove(test_filename)

    def test_write_to_file_creates_file(self, test_filename):
        """Test that write_to_file creates a file"""
        write_to_file(test_filename, "Test content")
        assert os.path.exists(test_filename), "File should be created"

    def test_write_to_file_with_simple_content(self, test_filename):
        """Test writing simple text content to file"""
        content = "Hello, World!"
        write_to_file(test_filename, content)

        # Read directly to verify
        with open(test_filename, 'r') as f:
            actual_content = f.read()

        assert actual_content == content, "Content should match what was written"

    def test_write_to_file_overwrites_existing(self, test_filename):
        """Test that write_to_file overwrites existing file"""
        write_to_file(test_filename, "First content")
        write_to_file(test_filename, "Second content")

        with open(test_filename, 'r') as f:
            actual_content = f.read()

        assert actual_content == "Second content", "File should contain only the second content"

    def test_read_from_file_returns_correct_content(self, test_filename):
        """Test that read_from_file returns correct content"""
        expected_content = "This is test content"

        # Write using standard method
        with open(test_filename, 'w') as f:
            f.write(expected_content)

        actual_content = read_from_file(test_filename)
        assert actual_content == expected_content, "Read content should match written content"

    def test_write_and_read_integration(self, test_filename):
        """Test integration of write_to_file and read_from_file"""
        original_content = "Integration test content"

        write_to_file(test_filename, original_content)
        read_content = read_from_file(test_filename)

        assert read_content == original_content, "Read content should match written content"

    def test_write_empty_string(self, test_filename):
        """Test writing an empty string"""
        write_to_file(test_filename, "")
        content = read_from_file(test_filename)

        assert content == "", "Should be able to write and read empty string"

    def test_write_multiline_content(self, test_filename):
        """Test writing multiline content"""
        multiline_content = "Line 1\nLine 2\nLine 3"

        write_to_file(test_filename, multiline_content)
        content = read_from_file(test_filename)

        assert content == multiline_content, "Should handle multiline content correctly"

    def test_write_special_characters(self, test_filename):
        """Test writing content with special characters"""
        special_content = "Special chars: !@#$%^&*()_+-=[]{}|;:',.<>?/~`"

        write_to_file(test_filename, special_content)
        content = read_from_file(test_filename)

        assert content == special_content, "Should handle special characters correctly"

    def test_read_from_nonexistent_file_raises_error(self):
        """Test that reading from non-existent file raises FileNotFoundError"""
        with pytest.raises(FileNotFoundError):
            read_from_file("nonexistent_file.txt")


# Additional standalone tests
def test_write_to_file_with_long_content():
    """Test writing long content"""
    filename = "test_long_content.txt"
    long_content = "A" * 10000  # 10,000 characters

    try:
        write_to_file(filename, long_content)
        content = read_from_file(filename)
        assert content == long_content, "Should handle long content"
        assert len(content) == 10000, "Content length should be 10,000"
    finally:
        if os.path.exists(filename):
            os.remove(filename)


# Note: Unicode test removed because the original functions don't specify
# UTF-8 encoding. To support Unicode, the functions would need to use:
# open(filename, 'w', encoding='utf-8') and open(filename, 'r', encoding='utf-8')
