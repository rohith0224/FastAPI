import React, { useState } from 'react';

interface AddFruitFormProps {
  addFruit: (fruitName: string) => void;
}

const AddFruitForm: React.FC<AddFruitFormProps> = ({ addFruit }) => {
  const [fruitName, setFruitName] = useState<string>('');

  const handleSubmit = (event: React.FormEvent<HTMLFormElement>) => {
    event.preventDefault();
    if (fruitName.trim()) {
      addFruit(fruitName);
      setFruitName('');
    }
  };

  return (
    <form onSubmit={handleSubmit}>
      <input
        type="text"
        value={fruitName}
        onChange={(e: React.ChangeEvent<HTMLInputElement>) => setFruitName(e.target.value)}
        placeholder="Enter fruit name"
      />
      <button type="submit">Add Fruit</button>
    </form>
  );
};

export default AddFruitForm;
