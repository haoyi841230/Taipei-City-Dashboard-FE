<script setup>
import { ref, defineProps, onMounted } from "vue";
import VueApexCharts from "vue3-apexcharts";

const props = defineProps(["chart_config", "activeChart", "series"]);
console.warn("props", props);
const chartOptions = ref({
	series: props.series,
	chart: {
		height: 350,
		type: "line",
		toolbar: {
			show: false,
		},
		zoom: {
			enabled: false,
		},
	},
	stroke: {
		width: [0, 4],
	},
	dataLabels: {
		enabled: false,
		enabledOnSeries: [1],
	},
	labels: [
		"2015",
		"2016",
		"2017",
		"2018",
		"2019",
		"2020",
		"2021",
		"2022",
		"2023",
	],
	xaxis: {
		type: "datetime",
	},
	color: ["#ffffcc", "#ccffcc"],
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

const chartRef = ref(null);

onMounted(() => {
	// Access the chart instance using chartRef.value if needed
});
</script>

<template>
	<div v-if="activeChart === 'MixedCharts'">
		<vue-apex-charts
			:options="chartOptions"
			:series="
				props.series.map((s, index) => ({
					...s,
					type: index === 0 ? 'column' : 'line',
				}))
			"
			ref="chartRef"
		></vue-apex-charts>
	</div>
</template>
