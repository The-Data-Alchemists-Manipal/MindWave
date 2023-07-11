import torch
import torch.nn as nn
import torch.optim as optim
from torch.utils.data import DataLoader, Dataset

# Define the dataset class
class WordDataset(Dataset):
    def __init__(self, data):
        self.data = data

    def __len__(self):
        return len(self.data)

    def __getitem__(self, index):
        return self.data[index]

# Define the word embedding model
class WordEmbedding(nn.Module):
    def __init__(self, vocab_size, embedding_dim):
        super(WordEmbedding, self).__init__()
        self.embedding = nn.Embedding(vocab_size, embedding_dim)
        self.fc = nn.Linear(embedding_dim, 1)

    def forward(self, x):
        embedded = self.embedding(x)
        embedded = torch.mean(embedded, dim=1)
        output = self.fc(embedded)
        return output.squeeze(1)

# Prepare the data
data = ["This is Aman", "I am an Engineering Student", "I love coding", "I am contributing in GSSoC 2023"]
vocab = set(" ".join(data).split())
word_to_idx = {word: idx for idx, word in enumerate(vocab)}
idx_to_word = {idx: word for idx, word in enumerate(vocab)}
encoded_data = [[word_to_idx[word] for word in sentence.split()] for sentence in data]

# Convert data to PyTorch tensors
tensor_data = torch.LongTensor(encoded_data)

# Define hyperparameters
vocab_size = len(vocab)
embedding_dim = 10
learning_rate = 0.1
num_epochs = 100

# Create the dataset and data loader
dataset = WordDataset(tensor_data)
dataloader = DataLoader(dataset, batch_size=2, shuffle=True)

# Initialize the model and optimizer
model = WordEmbedding(vocab_size, embedding_dim)
optimizer = optim.Adam(model.parameters(), lr=learning_rate)
criterion = nn.BCEWithLogitsLoss()

# Training loop
for epoch in range(num_epochs):
    for batch in dataloader:
        inputs = batch[:, :-1]
        labels = batch[:, -1].unsqueeze(1).float()

        optimizer.zero_grad()

        outputs = model(inputs)
        loss = criterion(outputs, labels)

        loss.backward()
        optimizer.step()

    if (epoch + 1) % 10 == 0:
        print(f"Epoch {epoch+1}/{num_epochs}, Loss: {loss.item()}")

# Get the learned word embeddings
word_embeddings = model.embedding.weight.data

# Print the learned embeddings
for i, embedding in enumerate(word_embeddings):
    word = idx_to_word[i]
    print(f"{word}: {embedding}")
