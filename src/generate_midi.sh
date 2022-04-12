BUNDLE_PATH='~/Documents/genart/final_project/pretrained_models/attention_rnn.mag'
CONFIG='attention_rnn'
OUTPUT_PATH='~/Documents/genart/final_project/generated'

while read line
do
	echo "Got note_seq: ${line}"
	melody_rnn_generate \
	--config=${CONFIG} \
	--bundle_file=${BUNDLE_PATH} \
	--output_dir=${OUTPUT_PATH} \
	--num_outputs=1 \
	--num_steps=32 \
	--primer_melody="${line}"
	echo "playing notes..."
	echo "commented: pmidi -p 14:1 generated/*.mid"
	python3 play_midi.py ${OUTPUT_PATH}/*.mid
	rm ${OUTPUT_PATH}/*.mid
	echo "done"
done < "/dev/stdin"
