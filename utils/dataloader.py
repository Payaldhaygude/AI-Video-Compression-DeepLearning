import os
import cv2
import torch
from torch.utils.data import Dataset

class FrameDataset(Dataset):
    def __init__(self, frames_folder):
        self.frames_folder = frames_folder
        self.frame_files = sorted(os.listdir(frames_folder))

    def __len__(self):
        return len(self.frame_files)

    def __getitem__(self, idx):
        frame_path = os.path.join(self.frames_folder, self.frame_files[idx])

        img = cv2.imread(frame_path)

        # Convert BGR → RGB
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

        # Normalize (0–255 → 0–1)
        img = img / 255.0

        # Convert to tensor
        img = torch.tensor(img, dtype=torch.float32)

        # Change shape (H,W,C) → (C,H,W)
        img = img.permute(2, 0, 1)

        return img
    
if __name__ == "__main__":
    dataset = FrameDataset("data/processed_frames")

    print("Total frames:", len(dataset))

    sample = dataset[0]

    print("Tensor shape:", sample.shape)