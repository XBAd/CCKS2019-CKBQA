import os
from argparse import ArgumentParser

def get_args():
    bert_path="../../data/"
    parser = ArgumentParser(description = 'For KBQA')
    parser.add_argument("--data_dir",default='train_data',type=str)
    parser.add_argument("--bert_path",default=bert_path,type=str)
    parser.add_argument("--bert_model", default=bert_path+'bert-base-chinese.tar.gz', type=str)
    parser.add_argument("--bert_vocab", default=bert_path+'bert-base-chinese-vocab.txt', type=str)
    parser.add_argument("--syntax_embed_path", default='../data/%s.char.embed', type=str, help='path pattern for syntax embedding')
    parser.add_argument("--task_name",default='mrpc',type=str,help="The name of the task to train.")
    parser.add_argument("--output_dir",default='saved_syntax_word',type=str)
    ## Other parameters
    parser.add_argument("--cache_dir",default="",type=str,help="Where do you want to store the pre-trained models downloaded from s3")
    parser.add_argument("--max_seq_length",default=55,type=int)
    parser.add_argument("--do_train",default='true',help="Whether to run training.")
    parser.add_argument("--do_eval",default='true',help="Whether to run eval on the dev set.")
    parser.add_argument("--do_lower_case",action='store_false',help="Set this flag if you are using an uncased model.")
    parser.add_argument("--train_batch_size",default=32,type=int,help="Total batch size for training.")
    parser.add_argument("--batch_size",default=32,type=int,help="Total batch size.")
    parser.add_argument("--no_gpu",default=1,type=int,help="use no.th gpu")
    parser.add_argument("--eval_batch_size",default=32,type=int,help="Total batch size for eval.")
    parser.add_argument("--learning_rate",default=1e-5,type=float,help="The initial learning rate for Adam.")
    parser.add_argument("--num_train_epochs",default=100,type=float,help="Total number of training epochs to perform.")
    parser.add_argument("--warmup_proportion",default=0.1,type=float,)
    parser.add_argument("--no_cuda",action='store_true',help="Whether not to use CUDA when available")
    parser.add_argument("--local_rank",type=int,default=-1,help="local_rank for distributed training on gpus")
    parser.add_argument('--seed',type=int,default=42,help="random seed for initialization")
    parser.add_argument('--gradient_accumulation_steps',type=int,default=1,help="Number of updates steps to accumulate before performing a backward/update pass.")
    parser.add_argument('--server_ip', type=str, default='', help="Can be used for distant debugging.")
    parser.add_argument('--server_port', type=str, default='', help="Can be used for distant debugging.")
    ## lstm parameters
    parser.add_argument("--requires_grad",action='store_true',help="Whether not to use syntax")
    parser.add_argument("--use_syntax",action='store_true',help="Whether not to use syntax")
    parser.add_argument("--syntax_hidden_embed",action='store_true',help="Whether not to use embedding of syntax")
    parser.add_argument("--maxpooling",action='store_true',help="Whether not to use maxpooling")
    parser.add_argument("--avepooling",action='store_true',help="Whether not to use avepooling")
    parser.add_argument("--bert_embedding_size",default=768,type=int)
    parser.add_argument("--hidden_dim",default=300,type=int)
    parser.add_argument("--lstm_layer",default=1,type=int)
    parser.add_argument("--bilstm",action='store_true')
    parser.add_argument("--len_syntax_dict",default=30,type=int)
    parser.add_argument("--syntax_dim",default=50,type=int)
    parser.add_argument("--num_labels",default=4,type=int)
    parser.add_argument("--dropout",default=0.5,type=float)
    args = parser.parse_args()
    return args