# distilhubert-finetuned-gtzan

This model is a fine-tuned version of [ntu-spml/distilhubert](https://huggingface.co/ntu-spml/distilhubert) on the marsyas/gtzan dataset.
It achieves the following results on the evaluation set:
 Link: [Click Here](https://huggingface.co/itsindro/distilhubert-finetuned-gtzan)
- Loss: 0.5878
- Accuracy: 0.83

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 5e-05
- train_batch_size: 8
- eval_batch_size: 8
- seed: 42
- optimizer: Use adamw_torch with betas=(0.9,0.999) and epsilon=1e-08 and optimizer_args=No additional optimizer arguments
- lr_scheduler_type: linear
- num_epochs: 10
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step | Validation Loss | Accuracy |
|:-------------:|:-----:|:----:|:---------------:|:--------:|
| 1.978         | 1.0   | 113  | 1.4803          | 0.6      |
| 1.3816        | 2.0   | 226  | 1.0322          | 0.72     |
| 1.0378        | 3.0   | 339  | 0.9786          | 0.75     |
| 0.7748        | 4.0   | 452  | 0.7674          | 0.74     |
| 0.6074        | 5.0   | 565  | 0.6434          | 0.81     |
| 0.5075        | 6.0   | 678  | 0.5948          | 0.77     |
| 0.3899        | 7.0   | 791  | 0.5878          | 0.83     |
| 0.2387        | 8.0   | 904  | 0.5331          | 0.82     |
| 0.1927        | 9.0   | 1017 | 0.5601          | 0.83     |
| 0.1532        | 10.0  | 1130 | 0.5554          | 0.83     |


### Framework versions

- Transformers 4.48.0
- Pytorch 2.5.1+cu124
- Datasets 3.2.0
- Tokenizers 0.21.0
