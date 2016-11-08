# A Machine Learning LSTM Music Generator with RTTTL

Using lstm_generator_wrapper: https://github.com/cosimoiaia/lstm_generator_wrapper

RTTTL Specification: https://en.wikipedia.org/wiki/Ring_Tone_Transfer_Language

Trained Model: https://www.dropbox.com/s/vw2l1g9ydeervdj/model.tfl?dl=0

```bash
~/git/lstm_generator_wrapper$ ./lstm.py --dataset ringtones_raw.txt --hidden_layer_size 2 --max_sequence_lenght 32
MaxLen =  32
Vectorizing text...
Text total length: 2203411
Distinct chars: 107
Total sequences: 734460
Training model...
---------------------------------
Run id: ringtones_raw.txt
Log directory: /tmp/tflearn_logs/
---------------------------------
Training samples: 661014
Validation samples: 73446
--
Training Step: 5164  | total loss: 1.222461.27880
| Adam | epoch: 000 | loss: 1.22246 -- iter: 660992/661014
Training Step: 5165  | total loss: 1.23827
| Adam | epoch: 001 | loss: 1.23827 | val_loss: 1.21472 -- iter: 661014/661014
--
Saving trained model to file  model.tfl
-- Test with temperature of %f -- 1.0
bb1rci:8f5,8f5,e5,e5,g5,e5,f5,p,8a5,8a5,f5,a5,8c,8a5,f5,8e,8c.5,d#5
~/git/lstm_generator_wrapper$
```

First training with a very dirty dataset and a quite short Sequence lenght, however it took only 4h on a AMD FX(tm)-4350 Quad-Core and even with an high temperature, the generated results are not bad at all. LSTMs are really powerfull!
