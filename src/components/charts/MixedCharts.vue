<script setup>
import { ref, onMounted } from "vue";
import VueApexCharts from "vue-apexcharts";
const props = defineProps(["chart_config", "activeChart", "series"]);
console.log(props.series[0].data);
const chartOptions = ref({
	series: [
		{
			name: "Website Blog",
			type: "column",
			data: [440, 505, 414, 671, 227, 413, 201, 352, 752, 320, 257, 160],
			color: "#ffffcc",
		},
		{
			name: "Social Media",
			type: "line",
			data: [23, 42, 35, 27, 43, 22, 17, 31, 22, 22, 12, 16],
			color: "#ccffcc",
		},
	],
	chart: {
		height: 350,
		type: "line",
	},
	stroke: {
		width: [0, 4],
	},
	dataLabels: {
		enabled: false,
		enabledOnSeries: [1],
	},
	labels: [
		"01 Jan 2001",
		"02 Jan 2001",
		"03 Jan 2001",
		"04 Jan 2001",
		"05 Jan 2001",
		"06 Jan 2001",
		"07 Jan 2001",
		"08 Jan 2001",
		"09 Jan 2001",
		"10 Jan 2001",
		"11 Jan 2001",
		"12 Jan 2001",
	],
	xaxis: {
		type: "datetime",
	},
	color: "#ffffcc",
	yaxis: [
		{
			title: {
				text: "Website Blog",
			},
			color: "#ffffcc",
		},
		{
			opposite: true,
			title: {
				text: "Social Media",
			},
			color: "#ccffcc",
		},
	],
});

const chart = ref(null);
</script>

<template>
	<div v-if="activeChart === 'MixedCharts'">
		<apexchart
			type="line"
			height="350"
			:options="chartOptions"
			:series="series"
		></apexchart>
	</div>
</template>
